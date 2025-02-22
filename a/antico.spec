%undefine _debugsource_packages

Name: antico
Version: 0.2
Release: 6.1
Summary: A Qt4/X11 Desktop/Window Manager
Group: Graphical desktop/Other
License: GPL
URL: https://www.antico.netsons.org/
Source0: %name-%version.tar
Patch0: antico-0.2-alt-DSO.patch
BuildRequires: gcc-c++ libX11-devel qt4-devel libXext-devel

%description
The goal is to create a Desktop/Window manager simple and fast. All parameters must be configured from few files,
avoiding unnecessary complications, following the K.I.S.S. philosophy.
The whole project is based only on Qt4 libraries, without any other external dependencies (e.g. kdelibs ...).

%prep
%setup -q
%patch 0 -p1

%build
qmake-qt4
%make_build

%install
%make_install INSTALL_ROOT=%buildroot

%files
%doc README CHANGELOG
%_bindir/%name
%_datadir/%name

%changelog
* Tue Aug 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt6.gcbed547.1
- Fixed build
* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.2-alt6.gcbed547
- update from upstream
* Tue May 19 2009 Boris Savelev <boris@altlinux.org> 0.2-alt5.g5671eb2
- update from upstream
* Sat May 16 2009 Boris Savelev <boris@altlinux.org> 0.2-alt4.g94854be
- fix alt+tab bug (update from upstream)
* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 0.2-alt3.gddf647c
- fix #20004
* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 0.2-alt2.gd2d3ab2
- update from upstream
* Fri May 01 2009 Boris Savelev <boris@altlinux.org> 0.2-alt1
- intial build for Sisyphus
