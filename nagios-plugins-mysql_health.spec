%define debug_package %{nil}

Summary:	Nagios plugins to check the status of Mysql Servers
Name:		nagios-plugins-mysql
Version:	2.1.7
Release:	2%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://labs.consol.de/lang/en/nagios/check_mysql_health/
#Source1:	http://labs.consol.de/download/shinken-nagios-plugins/check_mysql_health-%{version}.tar.gz
Source0:	http://labs.consol.de/download/shinken-nagios-plugins/nagios-plugins-mysql-%{version}.tar.gz
Requires:	perl-Nagios-Plugin
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
check_mysql_health is a plugin, which is used to monitor different parameters of a MS SQL server.

%prep
%setup -T -b0 

%build
aclocal
autoconf
automake
./configure --libexecdir=%{_libdir}/nagios/plugins/ --libdir=%{_libdir}
make 


%install
make install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/nagios/plugins/check_mysql_health

%changelog
* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 2.1.7-2
- new package built with tito

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-6
- Initial packaging
