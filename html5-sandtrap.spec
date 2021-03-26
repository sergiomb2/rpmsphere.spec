Summary: Sandtrap in HTML5
Name: html5-sandtrap
Version: 20110116
Release: 1
License: freeware
Group: Amusements/Games
Source0: %{name}.zip
URL: http://gopherwoodstudios.com/sandtrap/sand-trap.htm
Requires: oxzilla
BuildArch: noarch

%description
The aim of the game - Sand Trap - is to move the grains of sand
to the desired location by rotating different containers.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=HTML5 Sandtrap
Comment=Physics game in HTML5
Categories=Game;ArcadeGame;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/bg.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -s 512x600 index.html
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Sep 24 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20100921-1
- Initial build
