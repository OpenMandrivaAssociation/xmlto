Summary:	A tool for converting XML files to various formats
Name:		xmlto
Version:	0.0.26
Release:	6
License:	GPLv2+

#Older versions up to xmlto-0.0.20
#URL: http://cyberelk.net/tim/xmlto/
#Source0: http://cyberelk.net/tim/data/xmlto/stable/%{name}-%{version}.tar.bz2
URL:		https://fedorahosted.org/xmlto/
Source0:	https://fedorahosted.org/releases/x/m/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	docbook-xsl >= 1.56.0
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	util-linux, flex

# We rely heavily on the DocBook XSL stylesheets!
Requires:	docbook-xsl >= 1.74.2
Requires:	xsltproc
Requires:	docbook-dtds
Requires:	util-linux
Requires:	flex

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%package tex
License:	GPLv2+
Summary:	A set of xmlto backends with TeX requirements
# For full functionality, we need passivetex.
Requires:	passivetex >= 1.11
# We require main package
Requires:	xmlto = %{version}-%{release}
BuildArch:	noarch


%description tex
This subpackage contains xmlto backend scripts which do require
PassiveTeX/TeX for functionality.

%package xhtml
License:	GPLv2+
Summary:	A set of xmlto backends for xhtml1 source format
# For functionality we need stylesheets xhtml2fo-style-xsl
Requires:	xhtml2fo-style-xsl
# We require main package
Requires:	xmlto = %{version}-%{release}
BuildArch:	noarch

%description xhtml
This subpackage contains xmlto backend scripts for processing
xhtml1 source format.

%prep
%setup -q

%build
%configure BASH=/bin/bash
%make

%check
make check

%install
%makeinstall_std


%files
%doc COPYING ChangeLog README AUTHORS NEWS
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto
%exclude %{_datadir}/xmlto/format/fo/dvi
%exclude %{_datadir}/xmlto/format/fo/ps
%exclude %{_datadir}/xmlto/format/fo/pdf
%exclude %dir %{_datadir}/xmlto/format/xhtml1/
%exclude %{_datadir}/xmlto/format/xhtml1


%files tex
%{_datadir}/xmlto/format/fo/dvi
%{_datadir}/xmlto/format/fo/ps
%{_datadir}/xmlto/format/fo/pdf

%files xhtml
%dir %{_datadir}/xmlto/format/xhtml1/
%{_datadir}/xmlto/format/xhtml1/*
