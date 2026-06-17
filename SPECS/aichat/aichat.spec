Name:           aichat
Version:        0.30.0
Release:        1%{?dist}
Summary:        All-in-one LLM CLI Tool
License:        MIT OR Apache-2.0

BuildRequires:  cargo
BuildRequires:  rust

%description
All-in-one LLM CLI Tool

Documentation: https://docs.rs/aichat/0.30.0
Homepage: https://github.com/sigoden/aichat
Repository: https://github.com/sigoden/aichat
Crates.io: https://crates.io/crates/aichat/0.30.0

aichat #chatgpt #llm #cli #ai #repl

%build
cargo install --force --locked "aichat" --version "0.30.0" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
strip ./release//bin/*
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

%files
%{_bindir}/*

%changelog
* Sat May 23 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.30.0-1
- Initial package creation
