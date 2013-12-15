# sensu-report
[![Build Status](https://travis-ci.org/solarkennedy/sensu-report.png)](https://travis-ci.org/solarkennedy/sensu-report)

A script to query the [Sensu API](http://sensuapp.org/docs/0.12/api)
and get a human readable report.

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

