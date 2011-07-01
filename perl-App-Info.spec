%define upstream_name	 App-Info
%define upstream_version 0.57

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
