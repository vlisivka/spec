Name:           gptop
Version:        0.2.0
Release:        1%{?dist}
Summary:        A cross-platform GPU monitor TUI with support for both Apple Silicon and NVIDIA GPUs.
License:        GPL-3.0

BuildRequires:  cargo
BuildRequires:  rust

%description
A cross-platform GPU monitor TUI with support for both Apple Silicon and NVIDIA GPUs.

Documentation: https://docs.rs/gptop/0.2.0
Homepage: https://github.com/evilsocket/gptop
Repository: https://github.com/evilsocket/gptop
Crates.io: https://crates.io/crates/gptop/0.2.0

gptop #gpu #monitor #tui #apple-silicon #nvidia

%build
cargo install --force --locked "gptop" --version "0.2.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Tue Jun 23 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.2.0-1
- Initial package creation
