%define upstream_name	 App-Info
%define upstream_version 0.57

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	Information about software packages on a system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Pod) >= 1.20
BuildRequires:  apache
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:	sqlite3-tools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
App::Info provides a generalized interface for providing metadata
about software packages installed on a system. The idea is that
App::Info subclasses can be used in Perl application installers in
order to determine whether software dependencies have been fulfilled,
and to get necessary metadata about those software packages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build
./Build test

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README.md
%{perl_vendorlib}/App
%{_mandir}/*/*


%changelog
* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.570.0-1mdv2011.0
+ Revision: 688477
- new version

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.560.0-1
+ Revision: 639628
- update to new version 0.56

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2010.0
+ Revision: 402976
- rebuild using %%perl_convert_version

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2009.0
+ Revision: 238724
- update to new version 0.55

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdv2009.0
+ Revision: 209318
- update to new version 0.54

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2009.0
+ Revision: 201958
- update to new version 0.53

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdv2008.0
+ Revision: 63918
- update to new version 0.52

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.51-1mdv2008.0
+ Revision: 19183
-New version


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.49-1mdv2007.0
+ Revision: 73277
- import perl-App-Info-0.49-1mdk

* Fri Apr 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.49-1mdk
- New release 0.49
- better source URL
- use Module::Build everywhere
- minor spec cleanups
- better buildrequires syntax

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.48-1mdk
- 0.48

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.47-1mdk
- New release 0.47

* Mon Nov 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdk
- New release 0.45
- spec cleanup
- better summary
- use manual dependency syntax for buildrequires

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.44-1mdk
- initial Mandriva package, slight fedora import

