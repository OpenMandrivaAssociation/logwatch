Summary: 	Analyzes and Reports on system logs
Name: 		logwatch
Version: 	7.3.6
Release: 	%mkrel 2
License: 	MIT
Group: 		Monitoring
URL: 		http://www.logwatch.org
BuildArch: 	noarch
Source: 	ftp://ftp.kaybee.org/pub/linux/%{name}-%{version}.tar.bz2
Patch0:		logwatch-fixpath.patch
Requires: 	perl,coreutils,grep,mailx


%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.


%prep
%setup
%patch -p0

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
chmod 644 License

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
%doc License project/CHANGES project/TODO
