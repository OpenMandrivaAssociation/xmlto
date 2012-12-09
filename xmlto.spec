%define backend		passivetex

Summary: A tool for converting XML files to various formats
Name: xmlto
Version: 0.0.25
Release: 2
License: GPLv2+
Group: Publishing
URL: https://fedorahosted.org/xmlto/
Source0: https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
BuildRequires: docbook-xsl >= 1.56.0
BuildRequires: libxslt-proc
BuildRequires: docbook-dtd42-xml
# We rely entirely on the DocBook XSL stylesheets!
Requires: docbook-xsl >= 1.56.0
%if %{backend} == passivetex
# For full functionality, we need passivetex.
Requires:	xmltex
%else
Requires:	fop
%endif
Requires: libxslt-proc
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
rm -rf %{buildroot}
%makeinstall

[ -d %{buildroot}%{_datadir}/xmlto/xsl ] || \
  mkdir %{buildroot}%{_datadir}/xmlto/xsl

%files
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto


%changelog
* Sun Dec 11 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.25-2
+ Revision: 740266
- added requires on docbook-dtd412-xml and docbook-dtd45-xml to fix build problems with for example systemtap and abrt (pcpa)
- various fixes

* Mon Dec 05 2011 Götz Waschk <waschk@mandriva.org> 0.0.25-1
+ Revision: 737730
- new version

* Mon Jul 18 2011 Götz Waschk <waschk@mandriva.org> 0.0.24-1
+ Revision: 690222
- new version

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.0.23-5
+ Revision: 653247
- use passivetex as backend

* Thu Mar 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.0.23-4
+ Revision: 643674
- Change default backend to fop (pdf and ps output)
  CCBUG: 6139

* Thu Dec 02 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.0.23-3mdv2011.0
+ Revision: 604920
- Require docbook-dtd44-xml too so we can convert more documents without
  accessing the web to download the .dtd files

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.23-2mdv2010.1
+ Revision: 519083
- rebuild

* Wed Sep 23 2009 Götz Waschk <waschk@mandriva.org> 0.0.23-1mdv2010.0
+ Revision: 447653
- new version
- fix source URL

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 0.0.22-1mdv2010.0
+ Revision: 368983
- new version

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.0.21-1mdv2009.0
+ Revision: 271735
- new version
- update license
- update URL

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.0.20-2mdv2009.0
+ Revision: 266142
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 0.0.20-1mdv2009.0
+ Revision: 192389
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.0.18-5mdv2008.1
+ Revision: 130327
- kill re-definition of %%buildroot on Pixel's request


* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 0.0.18-5mdv2007.0
+ Revision: 108263
- Import xmlto

* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 0.0.18-5mdv2007.1
- Rebuild

* Sat May 06 2006 G�tz Waschk <waschk@mandriva.org> 0.0.18-4mdk
- disable Suggests for now

* Tue Jan 10 2006 G�tz Waschk <waschk@mandriva.org> 0.0.18-3mdk
- requires lynx instead of w3m, as lynx is in main

* Fri Feb 04 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.0.18-2mdk
- rebuild

* Thu Jan 22 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.0.18-1mdk
- new version

