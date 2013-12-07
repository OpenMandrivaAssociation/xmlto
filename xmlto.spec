%define backend		passivetex

Summary: A tool for converting XML files to various formats
Name: xmlto
Version: 0.0.25
Release: 5
License: GPLv2+
Group: Publishing
URL: https://fedorahosted.org/xmlto/
Source0: https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
BuildRequires: docbook-xsl >= 1.56.0
BuildRequires: libxslt-devel
BuildRequires: xsltproc
BuildRequires: docbook-dtd42-xml
# We rely entirely on the DocBook XSL stylesheets!
Requires: docbook-xsl >= 1.56.0
%if %{backend} == passivetex
# For full functionality, we need passivetex.
Requires:	xmltex
%else
Requires:	fop
%endif
Requires: xsltproc
Requires: docbook-dtd412-xml
Requires: docbook-dtd42-xml
Requires: docbook-dtd44-xml
Requires: docbook-dtd45-xml
Requires: lynx

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%prep
%setup -q

%build
%configure2_5x --with-backend=%{backend}
%make
make check

%install
%makeinstall

[ -d %{buildroot}%{_datadir}/xmlto/xsl ] || \
  mkdir %{buildroot}%{_datadir}/xmlto/xsl

%files
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto
