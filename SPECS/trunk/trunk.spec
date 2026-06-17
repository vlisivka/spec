Name:           trunk
Version:        0.22.0.beta.1
Release:        1%{?dist}
Summary:        Build, bundle & ship your Rust WASM application to the web.
License:        MIT/Apache-2.0

BuildRequires:  cargo
BuildRequires:  rust >= 1.90.0

%description
Build, bundle & ship your Rust WASM application to the web.

Documentation: https://docs.rs/trunk/0.22.0-beta.1

Repository: https://github.com/trunk-rs/trunk
Crates.io: https://crates.io/crates/trunk/0.22.0-beta.1

trunk #wasm #bundler #web #build-tool #compiler

%build
cargo install --force --locked "trunk" --version "0.22.0-beta.1" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Wed Jun 17 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.22.0-beta.1-1
- Initial package creation
