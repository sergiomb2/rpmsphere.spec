%global debug_package %{nil}

Name: 		edelib
Version:    2.0
#Version: 	2.1
Release: 	52.1
Source: 	http://sourceforge.net/projects/ede/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Summary:	A stable, small and fast cross-platform GUI ToolKit
URL: 		http://ede.sourceforge.net
License: 	LGPL
Group: 		System/Libraries
BuildRequires: fltk13-devel
BuildRequires: gcc-c++, jam, gettext, dbus-devel, doxygen, libpng-devel, libjpeg-devel

%description
Equinox Desktop Environment Library (edelib)
is a cross-platform C++ GUI toolkit for UNIX®/Linux® (X11),
Microsoft® Windows®, and MacOS® X. edelib provides modern GUI
functionality without the bloat and supports 3D graphics via
OpenGL® and its built-in GLUT emulation. It is currently maintained
by a small group of developers across the world with a central
repository on SourceForge.

%package devel
Summary: Header files and libraries for developing apps which will edelib
Version: 	%{version}
Release: 	52.1
Group: 		Development/C++
Requires: 	%{name} = %{version}
Provides:	edelib-devel

%description devel
The edelib-devel package contains the header files and libraries needed
to develop programs that use the edelib libraries.

%prep
%setup -q
sed -i -e 3597d -e 3600d configure

%build
export LIBS="-lX11"
./configure --prefix=$RPM_BUILD_ROOT/usr --libdir=$RPM_BUILD_ROOT%{_libdir}
sed -i 's|%{buildroot}||' *.pc edelib/edelib-config.h
jam

%install
jam install
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_libdir}/lib*
%{_libdir}/edelib

%files devel
%{_datadir}/doc/edelib-*
%{_libdir}/pkgconfig/edelib*.pc
%{_includedir}/*
%{_bindir}/edelib-*

%changelog
* Mon May 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Sat Jan 29 2005 Vedran Ljubovic <vljubovic@smartnet.ba> 2.0.2-1ede
- fix reversed logic w. efltk & efltk-devel
- create separate packages for efluid, ecalc and etranslate
- some other minor improvements
* Thu Jan 01 2004 nobody <nobody@nobody> 2.0.1.1-1
- Initial autogenerated release
