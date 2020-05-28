Example of a syslog drain

1) Deploy to Cloud Foundry
2) `cf create-user-provided-service syslogdrain -l SYSLOGDRAIN_URL`
3) `cf bind-service APPNAME syslogdrain`
4) restage your application
