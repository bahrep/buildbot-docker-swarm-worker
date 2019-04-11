from buildbot.plugins import worker


def test_import_from_plugins():
    worker.DockerSwarmLatentWorker("worker", "cjolowicz/buildbot-worker-example:1.8.0")
