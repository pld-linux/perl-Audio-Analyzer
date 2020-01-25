#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Audio
%define	pnam	Analyzer
Summary:	Audio::Analyzer - analyzing music files with FFT
Summary(pl.UTF-8):	Audio::Analyzer - analiza plików dźwiękowych przy użyciu FFT
Name:		perl-Audio-Analyzer
Version:	0.21
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a82fd16a5b8a09a8fa54fa5ba846d194
URL:		http://search.cpan.org/dist/Audio-Analyzer/
BuildRequires:	perl-Math-FFT
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it easy to analyze music files with the Fast Fourier
Transform and sync the output of the FFT in time for visual
representation.

%description -l pl.UTF-8
Ten moduł ułatwia analizę plików muzycznych przy użyciu szybkiej
transformaty Fouriera i synchronizację wyjścia FFT w czasie w celu
reprezentacji graficznej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/*.pm
%{_mandir}/man3/*
