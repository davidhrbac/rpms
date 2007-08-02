# $Id$
# Authority: dries
# Upstream: Jonas B. Nielsen <jonasbn$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Holidays

Summary: Object Oriented classes for holidays
Name: perl-Date-Holidays
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Holidays/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JONASBN/Date-Holidays-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
A package with object oriented classes for holidays.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Date::Holidays*
%{perl_vendorlib}/Date/Holidays.pm
%{perl_vendorlib}/Date/Holidays/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
