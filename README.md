# sensu-report
[![Build Status](https://travis-ci.org/solarkennedy/sensu-report.png)](https://travis-ci.org/solarkennedy/sensu-report)

Prints a human readable output of the failing Sensu checks into your terminal.
Queries the [Sensu API](http://sensuapp.org/docs/0.12/api)  and formats it 
into pretty colors. Basically a text based report of the sensu dashboard, 
on a particular client. (by default, the local hostmame)

## Examples

```
./sensu-report --server localhost

Failed Sensu checks on this host:
 [91mCrit: (6 hours ago) apt-get_update: [0mHit http://archive.ubuntu.com precise-...
 [91mCrit: (3 hours ago) check-ping-leb2.xkyle.com: [0mPING CRITICAL - Packet loss...
 [91mCrit: (3 hours ago) check-ping-remina.gateway.2wire.net: [0mCRITICAL - Networ...
```


## Put it in Puppet for MOTDs

```puppet
file { '/usr/bin/sensu_report':
  mode   => '0555',
  source => 'puppet:///files/sensu/sensu_report',
} ->
cron { 'sensu_report':
  command => "/usr/bin/sensu_report -s $sensu_api_server > /etc/motd",
  minute  => fqdn_rand(60),
} ->
sensu::check { "sensu_report":
  handlers    => 'default',
  command     => '/usr/lib/nagios/plugins/check_file_age -w 7200 -c 21600 -f /etc/motd',
  subscribers => 'sensu-test'
}
```

## Support

Open an [issue](https://github.com/solarkennedy/sensu-report/issues) or
[fork](https://github.com/solarkennedy/sensu-report/fork) and open a
[Pull Request](https://github.com/solarkennedy/sensu-report/pulls)

