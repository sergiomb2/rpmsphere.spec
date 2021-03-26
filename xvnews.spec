%global debug_package %{nil}

Name: xvnews
License: Distributable
Group: Networking/Mail
Version: 2.3.4
Release: 14.2
Summary: A News reader based on Openlook
Source: %{name}-%{version}.tar.Z
Patch: xvnews-2.3.2.dif
BuildRequires: imake, xview-devel, libX11-devel, libtirpc-devel, inn-devel, byacc
Requires: xorg-x11-fonts-75dpi
URL: http://alumnus.caltech.edu/~mjackson/xvnews.html

%description
If you find trn too obscure, this news reader might save you a lot
of trouble when reading News. Requirements: access to an NNTP server.

%package -n libguide-devel
Summary:	Run-time libraries and development header files for DevGuide
Group:		Development/Other

%description -n libguide-devel
runtime libraries needed to compile and run applications
generated by SUN's Interface Builder DevGuide 

%prep
%setup -q
%patch -b .old
sed -i 's|, daylight|; int daylight|' getdate.y
sed -i 's|-lintl|-I/usr/include/tirpc -ltirpc|' Imakefile Makefile.dist
sed -i -e 's|#undef POSIX_REGEX|#define POSIX_REGEX|' -e 's|#define SVR4_REGEX|#undef SVR4_REGEX|' config.h
sed -i 's|union wait|int|' xv_init.c

%build
export OPENWINHOME=/usr/openwin
export IMAKEINCLUDE=-I/usr/share/X11/config
xmkmf -a
sed -i 's|bison -y|yacc|' Makefile
make

%install
export OPENWINHOME=/usr/openwin
export HELPPATH=$OPENWINHOME/lib/help
make  DESTDIR="$RPM_BUILD_ROOT"  MANPATH=%{_mandir} install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/$HELPPATH
cp -a xvnews.1 $RPM_BUILD_ROOT/%{_mandir}/man1/xvnews.1x
cp -a xvnews.info $RPM_BUILD_ROOT/$HELPPATH

make -C guide install DESTDIR="$RPM_BUILD_ROOT" USRLIBDIR=%{_libdir}
make -C guide/libguide install DESTDIR="$RPM_BUILD_ROOT" USRLIBDIR=%{_libdir}

mkdir -p $RPM_BUILD_ROOT/usr/include/guide/libguide/
install -m 644 guide/*.h $RPM_BUILD_ROOT/usr/include/guide
install -m 644 guide/libguide/*.h $RPM_BUILD_ROOT/usr/include/guide/libguide
( cd $RPM_BUILD_ROOT/usr/include/
ln -s guide/*.h .
ln -s guide/libguide/*.h .
)

# menu
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=XVNews 
Comment=Open Look style News Reader
Exec=%{name}
Terminal=false
Type=Application
Icon=gnome-news
Encoding=UTF-8
Categories=Application;Network;
EOF

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc CHANGES README TODO
/usr/openwin/lib/help/xvnews.*
%{_bindir}/xvnews
%{_mandir}/man1/xvnews.*
%{_datadir}/applications/%{name}.desktop

%files -n libguide-devel
%{_libdir}/*.a
%{_includedir}/guide/*.h
%{_includedir}/guide/libguide/*.h
%{_includedir}/*.h

%changelog
* Thu Dec 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.4
- Rebuild for Fedora
* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.3.2-6mdk
- rebuild
* Sat Nov 23 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.3.2-5mdk
- add missing files
* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.3.2-4mdk
- rebuild
* Fri Sep 28 2001 Philippe Libat <philippe@mandrakesoft.com> 2.3.2-3mdk
- fix includedir
* Thu Sep 27 2001 Philippe Libat <philippe@mandrakesoft.com> 2.3.2-2mdk
- add libguide-devel
* Wed Sep 19 2001 Philippe Libat <philippe@mandrakesoft.com> 2.3.2-1mdk
- mandrakization
