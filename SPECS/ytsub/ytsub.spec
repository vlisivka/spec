Name:           ytsub
Version:        0.10.0
Release:        1%{?dist}
Summary:        A subscriptions only TUI Youtube client
License:        GPL-3.0

BuildRequires:  cargo
BuildRequires:  rust

%description
A subscriptions only TUI Youtube client

Documentation: https://docs.rs/ytsub/0.10.0

Repository: https://github.com/sarowish/ytsub
Crates.io: https://crates.io/crates/ytsub/0.10.0

ytsub #youtube #cli #tui #terminal

%build
cargo install --force --locked "ytsub" --version "0.10.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Wed Jun 17 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.10.0-1
- Initial package creation
