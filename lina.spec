%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name: lina
Summary: a LInux NAtive Forth
Version: 5.3.0
Release: 5
License: GPLv2
Group: Development/Languages
URL: http://home.hccnet.nl/a.w.m.van.der.horst/lina.html
Source0: http://home.hccnet.nl/a.w.m.van.der.horst/%{name}64-%{version}.tar.gz
Source1: ciarm.lina64-snapshot-6.87.tar.gz

%description
This is one of the Forth's that can be generated by the ciforth generic system.

%prep
%ifarch x86_64
%setup -q -n %{name}64-%{version}
%else
%setup -q -T -b 1 -n %{name}64-snapshot-6.87
%endif

%build
%ifarch x86_64
as -64 ci86.lina64.s
%else
as ciarm.lina64.s
%endif
ld -s -N a.out -o lina.bin

%install
install -Dm755 %{name}.bin %{buildroot}/usr/lib/%{name}.bin
install -Dm644 forth.lab %{buildroot}/usr/lib/forth.lab
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%post
cd /usr/lib
./%{name}.bin -g 60 %{name}
./%{name} -i /usr/bin/%{name} /usr/lib/forth.lab

%postun
rm -f /usr/bin/%{name} /usr/lib/%{name}

%files
%ifarch x86_64
%doc COPYING READMElina.txt ci86.lina64.* hellow.frt mywc32 mywc64 wc.script
%else
%doc COPYING READMElina.txt ciarm.lina64.* hellow.frt
%endif
#{_bindir}/*
%{_mandir}/man1/%{name}.1*
/usr/lib/%{name}.bin
/usr/lib/forth.lab

%changelog
* Fri Aug 16 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.0
- Rebuild for Fedora
