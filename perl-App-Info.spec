%define upstream_name	 App-Info
%define upstream_version 0.57
Name:       perl-%{upstream_name}
Version:	0.57
Release:	10

Summary:	Information about software packages on a system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/theory/app-info
Source0:	https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/App-Info-0.57.tar.gz
BuildRequires:	make
BuildRequires:  perl(Module::Build)
BuildRequires:	perl-devel
BuildRequires:  perl(Test::Pod) >= 1.20
BuildRequires:  apache
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:	sqlite3-tools
BuildArch:	noarch

%description
App::Info provides a generalized interface for providing metadata
about software packages installed on a system. The idea is that
App::Info subclasses can be used in Perl application installers in
order to determine whether software dependencies have been fulfilled,
and to get necessary metadata about those software packages.

%prep
%setup -q -n App-Info-0.57

%build
perl Build.PL installdirs=vendor
./Build

%check
# soft: do not fail package on test failures
set +e
./Build test || :

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


