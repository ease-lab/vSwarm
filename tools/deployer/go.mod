module github.com/ease-lab/vSwarm/tools/deployer

go 1.16

replace github.com/ease-lab/vSwarm/tools/endpoint => ../endpoint

require (
	github.com/ease-lab/vSwarm/tools/endpoint v0.0.0-00010101000000-000000000000
	github.com/sirupsen/logrus v1.8.1
)
