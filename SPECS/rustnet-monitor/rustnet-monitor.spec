Name:           rustnet-monitor
Version:        1.3.0
Release:        1%{?dist}
Summary:        A cross-platform network monitoring terminal UI tool built with Rust
License:        Apache-2.0

BuildRequires:  cargo
BuildRequires:  rust >= 1.88.0

%description
A cross-platform network monitoring terminal UI tool built with Rust

Documentation: https://docs.rs/rustnet-monitor
Homepage: https://github.com/domcyrus/rustnet
Repository: https://github.com/domcyrus/rustnet
Crates.io: https://crates.io/crates/rustnet-monitor/1.3.0

rustnet-monitor #network #monitoring #tui #ebpf #packet-capture

%build
cargo install --force --locked "rustnet-monitor" --version "1.3.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Sat May 23 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 1.3.0-1
- Initial package creation
