Name:           ast-grep
Version:        0.43.0
Release:        2%{?dist}
Summary:        Search and Rewrite code at large scale using precise AST pattern
License:        MIT
URL:            https://ast-grep.github.io/

BuildRequires:  cargo
BuildRequires:  rust >= 1.79

%description
Search and Rewrite code at large scale using precise AST pattern

Documentation: https://ast-grep.github.io/guide/introduction.html
Homepage: https://ast-grep.github.io/
Repository: https://github.com/ast-grep/ast-grep
Crates.io: https://crates.io/crates/ast-grep/0.43.0

ast-grep #ast #pattern #codemod #search #rewrite

%build
cargo install --force --locked "ast-grep" --version "0.43.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

# File /usr/bin/sg conflicts with same file from shadow-utils package
rm "%{buildroot}%{_bindir}/sg"

%files
%{_bindir}/*

%changelog
* Wed Jun 17 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.43.0-2
- Remove sg.
* Sun Jun 14 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.43.0-1
- Initial package creation
