Name:           cargo-crap
Version:        0.2.2
Release:        1%{?dist}
Summary:        Change Risk Anti-Patterns (CRAP) metric for Rust projects
License:        MIT

BuildRequires:  cargo
BuildRequires:  rust >= 1.88

%description
Change Risk Anti-Patterns (CRAP) metric for Rust projects

Documentation: https://docs.rs/cargo-crap
Homepage: https://github.com/minikin/cargo-crap
Repository: https://github.com/minikin/cargo-crap
Crates.io: https://crates.io/crates/cargo-crap/0.2.2

cargo-crap #cargo #code-quality #coverage #complexity #metrics

%build
cargo install --force --locked "cargo-crap" --version "0.2.2" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Wed Jun 10 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.2.2-1
- Initial package creation
