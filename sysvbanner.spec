%global debug_package %{nil}

Name: sysvbanner
Summary: System-V banner clone
Version: 1.0.15
Release: 3.1
Group: misc
URL: http://git.ryan52.info/?p=sysvbanner;a=summary
License: Public Domain
Source0: %{name}_%{version}.tar.gz

%description
Displays a `banner' text the same way as the System V banner does: horizontally.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc debian/changelog debian/copyright
%{_bindir}/banner
%{_mandir}/man1/banner.1.*

%changelog
* Thu Jun 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.15
- Rebuild for Fedora
