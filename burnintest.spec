%global __arch_install_post %{nil}
%global debug_package %{nil}

Summary: 	PC Reliability and Load Testing
Name: 		burnintest
Version: 	4.1
Release: 	1.bin
License: 	Commercial, free 30 day evaluation
Group:		Hardware/Tools
Source0:	https://www.passmark.com/downloads/bitlinux.tar.gz
Source1:	%{name}.desktop
Source2:        %{name}.png
URL:		http://www.passmark.com/products/burnintest/
Requires:	libcurl
Requires:       qt5-qtbase-gui

%description
PassMark BurnInTest™ is a software tool that allows all the major sub-systems
of a computer to be simultaneously stress tested for endurance, reliability
and stability.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
%ifarch x86_64
cp 64bit/* %{buildroot}%{_libexecdir}/%{name}
ln -s ../libexec/%{name}/bit_gui_x64 %{buildroot}%{_bindir}/%{name}
ln -s ../libexec/%{name}/bit_cmd_line_x64 %{buildroot}%{_bindir}/%{name}-cli
%else
cp 32bit/* %{buildroot}%{_libexecdir}/%{name}
ln -s ../libexec/%{name}/bit_gui_x32 %{buildroot}%{_bindir}/%{name}
ln -s ../libexec/%{name}/bit_cmd_line_x32 %{buildroot}%{_bindir}/%{name}-cli
%endif
chmod 777 %{buildroot}%{_libexecdir}/%{name}/savedkey.dat
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc B* readme.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1
- Initial binary package
