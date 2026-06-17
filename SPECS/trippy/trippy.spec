Name:           trippy
Version:        0.13.0
Release:        1%{?dist}
Summary:        A network diagnostic tool
License:        Apache-2.0

BuildRequires:  cargo
BuildRequires:  rust >= 1.78

%description
A network diagnostic tool

Documentation: https://github.com/fujiapple852/trippy
Homepage: https://github.com/fujiapple852/trippy
Repository: https://github.com/fujiapple852/trippy
Crates.io: https://crates.io/crates/trippy/0.13.0

trippy #cli #tui #traceroute #ping #icmp

%build
cargo install --force --locked "trippy" --version "0.13.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Sat May 23 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.13.0-1
- Initial package creation
