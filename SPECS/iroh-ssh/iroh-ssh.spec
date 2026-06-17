Name:           iroh-ssh
Version:        0.2.12
Release:        2%{?dist}
Summary:        ssh without ip by key over iroh.
License:        MIT
BuildArch:      %{_arch}
URL:            https://github.com/futpib/iroh-ssh

BuildRequires:  cargo
BuildRequires:  rust

Source0: iroh-ssh-server.service

%description
ssh without ip by key over iroh

%build
cargo install --force --locked "iroh-ssh" --version "0.2.12" --root "./release"

%install
mkdir -p "%{buildroot}%{_bindir}"
find ./release/bin -type f -exec strip {} +
mv -f ./release/bin/* "%{buildroot}%{_bindir}/"

mkdir -p "%{buildroot}%{_unitdir}"
cat %{SOURCE0} > "%{buildroot}%{_unitdir}/iroh-ssh-server.service"

%files
%attr(0644,root,root) %{_unitdir}/iroh-ssh-server.service
%ghost %attr(0644,root,root) %{_unitdir}/multi-user.target.wants/iroh-ssh-server.service
%attr(0755,root,root) %{_bindir}/*

%changelog
* Wed Jun 17 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.2.12-2
- iroh-ssh-server.service is added.
* Wed Jun 17 2026 Cargo2Spec Generator <cargo2spec@vlisivka.github.com> - 0.2.12-1
- Initial package creation
