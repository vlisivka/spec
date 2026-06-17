Name:           cargo-llvm-cov
Version:        0.8.7
Release:        1%{?dist}
Summary:        Cargo subcommand to easily use LLVM source-based code coverage (-C instrument-coverage).
License:        Apache-2.0 OR MIT

BuildRequires:  cargo
BuildRequires:  rust >= 1.87

%description
Cargo subcommand to easily use LLVM source-based code coverage (-C instrument-coverage).

Documentation: https://docs.rs/cargo-llvm-cov/0.8.7

Repository: https://github.com/taiki-e/cargo-llvm-cov
Crates.io: https://crates.io/crates/cargo-llvm-cov/0.8.7

cargo-llvm-cov #cargo #coverage #subcommand #testing

%build
cargo install --force --locked "cargo-llvm-cov" --version "0.8.7" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Wed Jun 10 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.8.7-1
- Initial package creation
