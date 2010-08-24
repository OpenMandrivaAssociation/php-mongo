%define modname mongo
%define dirname %{modname}
%define soname %{modname}.so
%define inifile B04_%{modname}.ini

Summary:	Mongo Database Driver
Name:		php-%{modname}
Version:	1.0.9
Release:	%mkrel 1
Group:		Development/PHP
License:	Apache License
URL:		http://pecl.php.net/package/mongo/
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

