%define _default_patch_fuzz 2

Name:           hypermail
BuildRequires:  httpd-devel bison gdbm-devel apr-util-devel pcre-devel libdb-devel
License:        GPL v2 or later
Group:          Productivity/Networking/Email/Utilities
Version:        2.4.0
Release:        1
URL:            http://www.hypermail-project.org/
Summary:        Convert Mail Archives in mailbox Format to HTML Pages
Source:         https://sourceforge.net/projects/hypermail/files/hypermail/%{version}/hypermail-%{version}.tar.gz
Patch:          hypermail-2.1.8-docs.patch
Patch1:         hypermail-2.1.8-s390.patch
#Patch2:         hypermail-setup.patch
Patch4:         hypermail-gcc4.diff
Patch5:         nonstaticpcre.patch
Patch6:         strip.patch
Patch7:         hypermail-2.2.0-comparison.diff
Patch9:         hypermail-2.2.0_bad-interpreter.patch
%define apache_serverroot /usr/share/httpd

%description
Hypermail is a program that takes a file of mail messages in mailbox
format and generates a set of cross-referenced HTML documents.	Each
file that is created represents a separate message in the mail archive
and contains links to other articles, so that the entire archive can be
browsed in a number of ways by following links.  Archives generated by
Hypermail can be incrementally updated, and Hypermail is set by default
to only update archives when changes are detected.

%package doc
License:        GPL v2 or later
Summary:        Hypermail Documentation
Group:          Productivity/Networking/Email/Utilities
Requires:       hypermail = %{version}
BuildArch:	noarch

%description doc
Documentation files for hypermail converter.

Authors:
--------
    Kevin Hughes <kevinh@eit.com>

%prep
%setup -q
#%patch
#%patch1
#%patch2 -p1
#%patch4
#%patch5
#%patch6
#%patch7
#find . -name CVS -type d | xargs rm -rf
#find . -type f | xargs chmod u+w
#%patch9

%build
#cp -f /usr/share/automake-*/config.guess .
#export CFLAGS="$RPM_OPT_FLAGS"
#rm -rf src/pcre
#libtoolize --force
#aclocal
#autoconf
#./configure --prefix=/usr \
#            --mandir=%{_mandir} --infodir=%{_infodir} \
#	    --with-htmldir=%{_defaultdocdir}/hypermail/docs \
#	    --with-httpddir=%{apache_serverroot}
#./configure --prefix=/usr
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/hypermail/docs
make prefix=$RPM_BUILD_ROOT/usr \
     mandir=$RPM_BUILD_ROOT/%{_mandir} \
     infodir=$RPM_BUILD_ROOT/%{_infodir} \
     htmldir=$RPM_BUILD_ROOT/%{_defaultdocdir}/hypermail/docs install
make -C src cgidir=$RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin mail.install
cp -vr contrib/ $RPM_BUILD_ROOT/%{_defaultdocdir}/hypermail/
rm docs/Makefile* docs/hmrc.4 docs/hypermail.1    # don't install these files in %files sect.

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_docdir}/hypermail/contrib/*.py %{buildroot}%{_docdir}/hypermail/contrib/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc KNOWN_BUGS README TODO UPGRADE Changelog
/usr/bin/hypermail
/usr/bin/msg2archive
/usr/bin/rdmsg
%{apache_serverroot}/cgi-bin/mail
%doc %{_mandir}/man1/hypermail.1.gz
%doc %{_mandir}/man4/hmrc.4.gz

%files doc
%{_docdir}/%{name}

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.0
- Rebuilt for Fedora
* Mon Nov 23 2009 pgajdos@suse.cz
- refreshed audit.patch to build with fuzz=0
* Mon Aug 31 2009 pgajdos@suse.cz
- build againist libdb-4_5 to fix build
* Fri Jan 30 2009 pgajdos@suse.cz
- splitted off doc package
* Wed Aug 20 2008 meissner@suse.de
- compile with regular RPM_OPT_FLAGS (unclear who set -O0)
* Thu May 24 2007 pgajdos@suse.cz
- fixed path to perl interpreter
- bad-interpreter.patch
* Thu Mar 29 2007 rguenther@suse.de
- Add bison BuildRequires.
* Mon Mar 26 2007 rguenther@suse.de
- Add gdbm-devel BuildRequires.
* Thu Feb  1 2007 mfabian@suse.de
- Bugzilla #98496: fix the encoding problems by updating to
  CVS HEAD (2.2.0.20070131).
- make not only "set_i18n = 1" but also "set_i18n_body = 1"
  the default to get everything converted to UTF-8.
- fix crashes on 64 bit systems.
* Tue Jan  2 2007 anicka@suse.cz
- fix comparison with string literal [#231197]
* Thu May 18 2006 schwab@suse.de
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Aug 26 2005 pnemec@suse.cz
- make hypermail use system pcre
* Tue Jul 26 2005 mfabian@suse.de
- update to 2.2.0.
* Sun May  1 2005 mmj@suse.de
- build with gcc4
* Mon Apr 19 2004 ro@suse.de
- build with apache2
* Fri Jan 16 2004 ro@suse.de
- fix build as user (apxs path)
* Sat Jan 10 2004 adrian@suse.de
- add %%defattr
* Thu Sep 18 2003 tcrhak@suse.cz
- use correct types in setup.c [bug #31238]
* Wed Jul 30 2003 tcrhak@suse.cz
- update to version 2.1.8
* Tue Jun 10 2003 ltinkl@suse.cz
- updated sources to 2.1.7
- fixed the patches, reviewed the audit patch
- fixed the erroneous Provides field
* Mon Feb 24 2003 tcrhak@suse.cz
- security fix for several security failures (patch audit)
- fixed setup.c and setup.h for 64 bit archs;
  treat environment variables holding octal numbers as octal
  numbers, not decimal ones (patch setup)
- removed patch trio, that had broken hypermail for versions
  older than 2.1.3
* Mon Jan  6 2003 tcrhak@suse.cz
- update to version 2.1.5
* Mon Aug  5 2002 prehak@suse.cz
- update to version 2.1.4
- adjusted documentation
* Thu Aug  1 2002 ro@suse.de
- adapt server-root
* Tue May 21 2002 ro@suse.de
- run suse_update_config also in src/pcre
* Mon Dec 10 2001 tcrhak@suse.cz
- update to version 2.1.3
* Wed Oct  3 2001 tcrhak@suse.cz
- fixed src/trio.c -> hypermail-2.1.2-trio.patch
- va_list passed occasionally as a reference
- because of (axp) gcc-3.0.1-18
* Wed Aug 29 2001 adostal@suse.cz
- fix %%build (use aclocal...)
- create s390 patch
* Fri Aug 17 2001 adostal@suse.cz
- update to version 2.1.2
- fix %%install and %%files (htmldir and doc)
* Mon Apr  9 2001 pblaha@suse.cz
- update on 2.1.0
* Fri Feb 23 2001 ro@suse.de
- changed neededforbuild <apache> to <apache apache-devel>
* Wed Nov 15 2000 pblaha@suse.cz
- rename to hypermail
* Mon May 15 2000 nadvornik@suse.cz
- added BuildRoot
- added URL
* Thu Apr 13 2000 ro@suse.de
- added mm to neededforbuild
* Fri Jan 21 2000 ro@suse.de
- specfile cleanup
* Thu Jan 20 2000 ro@suse.de
- update to 2.0beta29
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Sep 28 1998 ro@suse.de
- removed own version of strdup completely
* Sat Sep 26 1998 ro@suse.de
- dont redeclare/redefine strdup for glibc
* Tue Nov 11 1997 ro@suse.de
- fixed file-list
* Wed Oct 29 1997 ro@suse.de
- first suse version 1.02
