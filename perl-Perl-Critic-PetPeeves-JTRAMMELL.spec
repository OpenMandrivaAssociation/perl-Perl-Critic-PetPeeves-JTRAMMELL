%define upstream_name    Perl-Critic-PetPeeves-JTRAMMELL
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Prohibit superfluous initializations

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
Module 'Perl::Critic::PetPeeves::JTRAMMELL' provides policies that I want
that haven't already been implemented elsewhere. So far this is:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*





