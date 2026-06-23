Name:           egui_pinger
Version:        0.6.2
Release:        1%{?dist}
Summary:        Simple pinger for multiple servers with graph and jitter.
License:        GPL-3.0-or-later

BuildRequires:  cargo
BuildRequires:  rust

Source0:        com.github.vlisivka.EguiPinger.desktop
Source1:        com.github.vlisivka.EguiPinger.svg


%description
Simple pinger for multiple servers with graph and jitter.

Documentation: https://docs.rs/egui_pinger/0.6.2

Repository: https://github.com/vlisivka/egui_pinger
Crates.io: https://crates.io/crates/egui_pinger/0.6.2

egui_pinger #egui #ping

%build
cargo install --force --locked "egui_pinger" --version "0.6.2" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

mkdir -p "%{buildroot}/usr/share/applications/"
cat %{SOURCE0} > "%{buildroot}/usr/share/applications/com.github.vlisivka.EguiPinger.desktop"

mkdir -p "%{buildroot}/usr/share/icons/hicolor/scalable/apps/"
cat %{SOURCE1} > "%{buildroot}/usr/share/icons/hicolor/scalable/apps/com.github.vlisivka.EguiPinger.svg"

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) /usr/share/applications/com.github.vlisivka.EguiPinger.desktop
%attr(0644,root,root) /usr/share/icons/hicolor/scalable/apps/com.github.vlisivka.EguiPinger.svg


%changelog
* Sat Jun 20 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.6.2-1
- Initial package creation
