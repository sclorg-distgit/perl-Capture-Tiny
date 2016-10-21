%{?scl:%scl_package perl-Capture-Tiny}

Name:           %{?scl_prefix}perl-Capture-Tiny
Version:        0.42
Release:        2%{?dist}
Summary:        Capture STDOUT and STDERR from Perl, XS or external programs
License:        ASL 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Capture-Tiny/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
# PerlIO is optional
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(PerlIO::scalar)
# Test::Differences is optional
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.62
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
Capture::Tiny provides a simple, portable way to capture anything sent to
STDOUT or STDERR, regardless of whether it comes from Perl, from XS code or
from an external program. Optionally, output can be teed so that it is
captured while being passed through to the original handles. Yes, it even
works on Windows. Stop guessing which of a dozen capturing modules to use
in any particular situation and just use this one.

%prep
%setup -q -n Capture-Tiny-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes examples README Todo
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jul 20 2016 Petr Pisar <ppisar@redhat.com> - 0.42-2
- SCL

* Wed Jun 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-1
- 0.42 bump

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.24 rebuild

* Mon Feb 29 2016 Petr Šabata <contyk@redhat.com> - 0.36-1
- 0.36 bump

* Fri Feb 19 2016 Petr Šabata <contyk@redhat.com> - 0.34-1
- 0.34 bump, metadata changes only

* Fri Feb 19 2016 Petr Šabata <contyk@redhat.com> - 0.32-1
- 0.32 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.22 rebuild

* Mon May 18 2015 Petr Šabata <contyk@redhat.com> - 0.30-1
- 0.30 bump
- Windows fixes only

* Fri Feb 13 2015 Petr Šabata <contyk@redhat.com> - 0.28-1
- 0.28 bump

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 0.27-1
- 0.27 bump
- META changes only

* Tue Nov 04 2014 Petr Šabata <contyk@redhat.com> - 0.26-1
- 0.26 bump
- Test suite enhancements only

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.20 rebuild

* Mon Aug 18 2014 Petr Šabata <contyk@redhat.com> - 0.25-1
- 0.25 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Petr Šabata <contyk@redhat.com> - 0.24-1
- 0.24 bump, fix CVE-2014-1875

* Thu Oct 24 2013 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump

* Thu Sep 05 2013 Petr Šabata <contyk@redhat.com> - 0.22-4
- Avoid circular dependencies when bootstrapping (#1004376)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Perl 5.18 rebuild

* Thu Mar 28 2013 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Petr Pisar <ppisar@redhat.com> - 0.21-1
- 0.21 bump

* Thu Oct 04 2012 Petr Šabata <contyk@redhat.com> - 0.20-1
- 0.20 bump

* Wed Aug 08 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Perl 5.16 rebuild

* Mon May 07 2012 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Thu Feb 23 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Mon Feb 13 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump

* Mon Dec 05 2011 Petr Šabata <contyk@redhat.com> - 0.13-1
- 0.13 bump

* Fri Dec 02 2011 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-2
- Perl mass rebuild

* Fri May 20 2011 Petr Sabata <psabata@redhat.com> - 0.11-1
- 0.11 bump
- Removing defattr

* Wed Feb 09 2011 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump
- Remove BuildRoot stuff
- Migrate from Module::Build to ExtUtils::MakeMaker
- Install into perl core directory

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jun 21 2010 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump (bug #606277)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- Mass rebuild with perl-5.12.0

* Wed Jan 27 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-1
- update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-1
- update

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
