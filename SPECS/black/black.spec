Name:           black
Version:        26.5.1
Release:        1%{?dist}
Summary:        The uncompromising code formatter.
License:        Unknown
BuildArch:      x86_64

BuildRequires:  python3-pip
BuildRequires:  python3 >= 3.10

%description
The uncompromising code formatter.

_Black_ is the uncompromising Python code formatter. By using it, you agree to cede
control over minutiae of hand-formatting. In return, _Black_ gives you speed,
determinism, and freedom from `pycodestyle` nagging about formatting. You will save time
and mental energy for more important matters.
Blackened code looks the same regardless of the project you're reading. Formatting
becomes transparent after a while and you can focus on the content instead.
_Black_ makes code review faster by producing the smallest diffs possible.

Repository: https://github.com/psf/black

%build
: # nothing to build

%install
rm -rf %{buildroot}
python3 -m pip install --isolated --prefix="%{buildroot}%{_datadir}/black"   "black==%{version}" --compile --no-cache-dir

# Create symbolic links for each console script
mkdir -p %{buildroot}%{_bindir}
ln -srf %{buildroot}%{_datadir}/black/bin/black %{buildroot}%{_bindir}/black
ln -srf %{buildroot}%{_datadir}/black/bin/blackd %{buildroot}%{_bindir}/blackd

%clean
rm -rf %{buildroot}

%files
%{_datadir}/black/
%{_bindir}/black
%{_bindir}/blackd

%changelog
* Sun May 24 2026 Pip2Spec Generator <pip2spec@vlisivka.github.com> - 26.5.1-1
- Initial package creation
