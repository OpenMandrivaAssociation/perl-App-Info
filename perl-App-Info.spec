%define module	App-Info
%define name	perl-%{module}
%define version 0.49
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Information about software packages on a system
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/App/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:  perl-Module-Build
BuildRequires:  perl(Test::Pod) >= 1.20
BuildRequires:  apache
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:	sqlite3-tools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
App::Info provides a generalized interface for providing metadata
about software packages installed on a system. The idea is that
App::Info subclasses can be used in Perl application installers in
order to determine whether software dependencies have been fulfilled,
and to get necessary metadata about those software packages.

%prep
%setup -q -n %{module}-%{version} 

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
%doc Changes README
%{perl_vendorlib}/App
%{_mandir}/*/*



