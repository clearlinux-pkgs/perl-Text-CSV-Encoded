#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-CSV-Encoded
Version  : 0.25
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/Z/ZA/ZARQUON/Text-CSV-Encoded-0.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZA/ZARQUON/Text-CSV-Encoded-0.25.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-csv-encoded-perl/libtext-csv-encoded-perl_0.25-2.debian.tar.xz
Summary  : 'Encoding aware Text::CSV.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-CSV-Encoded-license = %{version}-%{release}
Requires: perl-Text-CSV-Encoded-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::CSV)

%description
=pod
=head1 NAME
Text::CSV::Encoded - Encoding aware Text::CSV.
=head1 SYNOPSIS
# Here in Perl 5.8 or later
$csv = Text::CSV::Encoded->new ({
encoding_in  => "iso-8859-1", # the encoding comes into   Perl
encoding_out => "cp1252",     # the encoding comes out of Perl
});

%package dev
Summary: dev components for the perl-Text-CSV-Encoded package.
Group: Development
Provides: perl-Text-CSV-Encoded-devel = %{version}-%{release}
Requires: perl-Text-CSV-Encoded = %{version}-%{release}

%description dev
dev components for the perl-Text-CSV-Encoded package.


%package license
Summary: license components for the perl-Text-CSV-Encoded package.
Group: Default

%description license
license components for the perl-Text-CSV-Encoded package.


%package perl
Summary: perl components for the perl-Text-CSV-Encoded package.
Group: Default
Requires: perl-Text-CSV-Encoded = %{version}-%{release}

%description perl
perl components for the perl-Text-CSV-Encoded package.


%prep
%setup -q -n Text-CSV-Encoded-0.25
cd %{_builddir}
tar xf %{_sourcedir}/libtext-csv-encoded-perl_0.25-2.debian.tar.xz
cd %{_builddir}/Text-CSV-Encoded-0.25
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-CSV-Encoded-0.25/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-CSV-Encoded
cp %{_builddir}/Text-CSV-Encoded-0.25/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-CSV-Encoded/8abdfcaaa2f121a1cd616bcb7838f2767fbbc74b
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-CSV-Encoded/70500cb8886ac705688eeedbdf90505ada368063
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::CSV::Encoded.3
/usr/share/man/man3/Text::CSV::Encoded::Coder::Base.3
/usr/share/man/man3/Text::CSV::Encoded::Coder::Encode.3
/usr/share/man/man3/Text::CSV::Encoded::Coder::EncodeGuess.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-CSV-Encoded/70500cb8886ac705688eeedbdf90505ada368063
/usr/share/package-licenses/perl-Text-CSV-Encoded/8abdfcaaa2f121a1cd616bcb7838f2767fbbc74b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
