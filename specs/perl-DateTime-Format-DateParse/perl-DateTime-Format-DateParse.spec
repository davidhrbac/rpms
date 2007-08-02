# $Id$
# Authority: dries
# Upstream: Joshua Hoblitt <jhoblitt$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-DateParse

Summary: Parses Date::Parse compatible formats
Name: perl-DateTime-Format-DateParse
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-DateParse/

Source: http://search.cpan.org//CPAN/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
This module is a compatibility wrapper around Date::Parse.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/DateParse.p*

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
