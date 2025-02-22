Name:           perl-Math-Random
Version:        0.72
Release:        2.1
Summary:        Random Number Generators
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            https://search.cpan.org/dist/Math-Random/
Source0:        https://www.cpan.org/modules/by-module/Math/Math-Random-%{version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Math::Random is a Perl port of the C version of randlib, which is a suite
of routines for generating random deviates. See "RANDLIB" for more
information.

%prep
%setup -q -n Math-Random-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes Index README README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Wed May 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.72
- Rebuilt for Fedora
* Wed Jun 18 2014 Josko Plazonic <plazonic@princeton.edu> 0.71-1
- Specfile autogenerated by cpanspec 1.78.
