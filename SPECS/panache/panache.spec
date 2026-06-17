Name:           panache
Version:        2.48.0
Release:        1%{?dist}
Summary:        An LSP, formatter, and linter for Markdown, Quarto, and R Markdown
License:        MIT

BuildRequires:  cargo
BuildRequires:  rust

%description
An LSP, formatter, and linter for Markdown, Quarto, and R Markdown

Documentation: https://docs.rs/panache/2.48.0
Homepage: https://panache.bz
Repository: https://github.com/jolars/panache
Crates.io: https://crates.io/crates/panache/2.48.0

panache #quarto #pandoc #markdown #formatter #language-server

%build
cargo install --force --locked "panache" --version "2.48.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Sat May 23 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 2.48.0-1
- Initial package creation
