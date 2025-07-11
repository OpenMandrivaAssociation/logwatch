Summary: 	Analyzes and Reports on system logs
Name: 		logwatch
Version: 	7.4.0
Release: 	5
License: 	MIT
Group: 		Monitoring
URL: 		https://www.logwatch.org
BuildArch: 	noarch
Source: 	http://downloads.sourceforge.net/project/logwatch/logwatch-7.4.0/logwatch-7.4.0.tar.gz
Patch0:		logwatch-fixpath.patch
Requires: 	perl,coreutils,grep,mailx
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.


%prep
%setup
%patch0 -p0

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/conf/logfiles
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/conf/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/scripts/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/scripts/shared
install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/lib

mkdir -p %{buildroot}/var/cache/%{name}

install -m 0755 scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/scripts/%{name}.pl
for i in scripts/logfiles/* ; do
   if [ $(ls $i | wc -l) -ne 0 ] ; then
      install -m 0755 -d %{buildroot}%{_sysconfdir}/log.d/$i
      install -m 0755 $i/* %{buildroot}%{_sysconfdir}/log.d/$i
   fi
done
install -m 0755 scripts/services/* %{buildroot}%{_sysconfdir}/log.d/scripts/services
install -m 0755 scripts/shared/* %{buildroot}%{_sysconfdir}/log.d/scripts/shared
install -m 0755 lib/* %{buildroot}%{_sysconfdir}/log.d/lib

install -m 0644 conf/*.conf %{buildroot}%{_sysconfdir}/log.d/conf
install -m 0644 conf/logfiles/* %{buildroot}%{_sysconfdir}/log.d/conf/logfiles
install -m 0644 conf/services/* %{buildroot}%{_sysconfdir}/log.d/conf/services

install -m 0755 -d %{buildroot}%{_mandir}/man8
install -m 0644 logwatch.8 %{buildroot}%{_mandir}/man8

rm -f %{buildroot}%{_sysconfdir}/log.d/%{name} \
   %{buildroot}%{_sysconfdir}/log.d/%{name}.conf \
   %{buildroot}%{_sysconfdir}/cron.daily/%{name} \
   %{buildroot}%{_sbindir}/%{name}

ln -s scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/%{name}
ln -s conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/%{name}.conf
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.daily
ln -s ../log.d/scripts/logwatch.pl %{buildroot}%{_sysconfdir}/cron.daily/0%{name}
install -m 0755 -d %{buildroot}%{_sbindir}
ln -s ../..%{_sysconfdir}/log.d/scripts/logwatch.pl %{buildroot}%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_sysconfdir}/log.d
%dir %{_sysconfdir}/log.d/conf
%dir %{_sysconfdir}/log.d/scripts
%dir %{_sysconfdir}/log.d/conf/logfiles
%dir %{_sysconfdir}/log.d/conf/services
%dir %{_sysconfdir}/log.d/scripts/logfiles
%dir %{_sysconfdir}/log.d/scripts/services
%dir %{_sysconfdir}/log.d/scripts/shared
%dir %{_sysconfdir}/log.d/scripts/logfiles/*
%dir %{_sysconfdir}/log.d/lib
%dir /var/cache/%{name}
%config(noreplace) %{_sysconfdir}/log.d/conf/*.conf
%config(noreplace) %{_sysconfdir}/log.d/conf/services/*
%config(noreplace) %{_sysconfdir}/log.d/conf/logfiles/*
%{_sysconfdir}/log.d/scripts/%{name}.pl
%{_sbindir}/%{name}
%{_sysconfdir}/log.d/scripts/shared/*
%{_sysconfdir}/log.d/scripts/services/*
%{_sysconfdir}/log.d/scripts/logfiles/*/*
%{_sysconfdir}/log.d/%{name}
%{_sysconfdir}/log.d/lib/Logwatch.pm
%{_sysconfdir}/log.d/%{name}.conf
%{_sysconfdir}/cron.daily/0%{name}
%doc %{_mandir}/man8/%{name}.8*


%changelog
* Sun Nov 13 2011 Alexander Khrukin <akhrukin@mandriva.org> 7.4.0-4mdv2012.0
+ Revision: 730311
- version update and spec files section fix

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 7.3.6-4mdv2009.0
+ Revision: 251372
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 7.3.6-2mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 7.3.6-2mdv2008.0
+ Revision: 70344
- fileutils, sh-utils & textutils have been obsoleted by coreutils a long time ago

* Thu Jul 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 7.3.6-1mdv2008.0
+ Revision: 55960
- new version

