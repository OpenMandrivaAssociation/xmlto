Summary: A tool for converting XML files to various formats
Name: xmlto
Version: 0.0.23
Release: %mkrel 2
License: GPLv2+
Group: Publishing
URL: https://fedorahosted.org/xmlto/
Source0: https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: docbook-xsl >= 1.56.0
BuildRequires: libxslt-proc
BuildRequires: docbook-dtd42-xml
# We rely entirely on the DocBook XSL stylesheets!
Requires: docbook-xsl >= 1.56.0
# For full functionality, we need passivetex.
Requires: xmltex
Requires: libxslt-proc
Requires: docbook-dtd42-xml
#gw for html->text either w3m, lynx or links are supported, w3m seems to be 
# the preferred application
#%if %mdkversion >= 200610
#Suggests: w3m
#%endif
Requires: lynx

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%prep
%setup -q

%build
%configure2_5x
%make
make check

%install
rm -rf %{buildroot}
%makeinstall

[ -d %{buildroot}%{_datadir}/xmlto/xsl ] || \
  mkdir %{buildroot}%{_datadir}/xmlto/xsl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto


