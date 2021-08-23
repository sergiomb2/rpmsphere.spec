%undefine _debugsource_packages
%global _version 12-2021.7

Summary: A language with roots in Forth
Name: retro
Version: 12.2021.7
Release: 1
License: Freeware
Group: Development/Language
URL: http://www.forthworks.com/retro
Source0: http://www.forthworks.com/retro/r/RETRO%{_version}.tar.gz

%description
Retro is a concatenative, stack based language with roots in Forth. It is
designed to be small, easily learned, and easily modified to meet specific
needs, it has been developed and refined through continual use by a small
community over the last decade.

%prep
%setup -q -n RETRO%{_version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install PREFIX=/usr MANDIR=%{_mandir}/man1 EXAMPLESDIR=%{_datadir}/RETRO12

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%{_docdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/RETRO12

%changelog
* Sun Aug 1 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 12.2021.7
- Rebuilt for Fedora
