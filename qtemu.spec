%global debug_package %{nil}

Name:          qtemu
Version:       1.0.5
Release:       10.1
Summary:       A graphical user interface for QEMU written in Qt4
Group:         Graphical Desktop/Applications/Utilities
URL:           http://qtemu.org/
Source:        http://switch.dl.sourceforge.net/sourceforge/qtemu/qtemu-%{version}.tar.bz2
License:       GPL
BuildRequires: libpng-devel
BuildRequires: gcc-c++ qt4-devel
BuildRequires: ghostscript-core ImageMagick

%description
QtEmu is a graphical user interface for QEMU written in Qt4.
It has the ability to run virtual operating systems on native systems.
This way you can easily test a new operating system or try a Live CD on your system without any troubles and dangers.

%prep
%setup -q

%build
qmake-qt4
make

%install
rm -rf "$RPM_BUILD_ROOT"
#%makeinstall
install -D -m0755 qtemu $RPM_BUILD_ROOT%{_datadir}/qtemu/qtemu
cp -a help translations $RPM_BUILD_ROOT%{_datadir}/qtemu/

install -d $RPM_BUILD_ROOT%{_bindir}
ln -s %{_datadir}/qtemu/qtemu $RPM_BUILD_ROOT%{_bindir}/qtemu

install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert images/qtemu.ico $RPM_BUILD_ROOT%{_datadir}/pixmaps/qtemu.png

# Create the system menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=QtEmu
Comment=A graphical interface for QEmu
Comment[it]=Interfaccia grafica per QEmu
GenericName=A graphical interface for QEmu
GenericName[it]=Interfaccia grafica per QEmu
Exec=qtemu
Icon=qtemu
Terminal=0
Type=Application
Categories=Application;Emulator;System;
X-KDE-StartupNotify=false
EOF

chmod 755 $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/qtemu
%{_datadir}/qtemu
%{_datadir}/applications/qtemu.desktop
%{_datadir}/pixmaps/qtemu.png
%doc COPYING ChangeLog README

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuild for Fedora
* Sun Jan 03 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.5-2mamba
- fixed desktop entry icon and category
* Tue Jan 27 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.5-1mamba
- automatic update by autodist
* Tue Aug 21 2007 Tiziana Ferro <tiziana.ferro@email.it> 1.0.4-2mamba
- Added system menu entry
* Sun Jul 22 2007 Tiziana Ferro <tiziana.ferro@email.it> 1.0.4-1mamba
- update to 1.0.4
* Sat Mar 10 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.2-1qilnx
- package created by autospec
