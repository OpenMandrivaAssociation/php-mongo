%define modname mongo
%define dirname %{modname}
%define soname %{modname}.so
%define inifile B04_%{modname}.ini

Summary:	Mongo Database Driver
Name:		php-%{modname}
Version:	1.2.10
Release:	3
Group:		Development/PHP
License:	Apache License
URL:		https://pecl.php.net/package/mongo/
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
Source1:	mongo.ini
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	apache-devel >= 2.2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package provides an interface for communicating with the Mongo database
in PHP.

%prep

%setup -q -n %{modname}-%{version}
[ "../package*.xml" != "/" ] && mv ../package*.xml .

cp %{SOURCE1} %{inifile}

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib}
%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/
install -m0644 %{inifile} %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README.md package*.xml 
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-2mdv2012.0
+ Revision: 795480
- rebuild for php-5.4.x

* Tue Apr 10 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-1
+ Revision: 790157
- 1.2.10

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-2
+ Revision: 761272
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1
+ Revision: 696381
- 1.2.4

* Sun Aug 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1
+ Revision: 695943
- 1.2.3

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2
+ Revision: 695444
- rebuilt for php-5.3.7

* Wed Jul 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1
+ Revision: 691889
- 1.2.2

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2
+ Revision: 646665
- rebuilt for php-5.3.6

* Wed Feb 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-1
+ Revision: 638029
- 1.1.4

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdv2011.0
+ Revision: 630309
- 1.1.3

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2011.0
+ Revision: 629839
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 628166
- ensure it's built without automake1.7

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2011.0
+ Revision: 618070
- 1.1.0

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-3mdv2011.0
+ Revision: 600512
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdv2011.0
+ Revision: 588850
- rebuild

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 1.0.10-1mdv2011.0
+ Revision: 582994
- update to new version 1.0.10

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 572565
- update to new version 1.0.9

* Mon Jul 26 2010 Funda Wang <fwang@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 560604
- new version 1.0.8

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdv2010.1
+ Revision: 514506
- 1.0.4

* Wed Jan 13 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 490650
- 1.0.3

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2010.1
+ Revision: 485409
- rebuilt for php-5.3.2RC1

* Sun Dec 27 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 482777
- 1.0.2

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2010.1
+ Revision: 468192
- rebuilt against php-5.3.1

* Sat Oct 03 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.0
+ Revision: 452914
- import php-mongo


* Sat Oct 03 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.0
- initial Mandriva package
