from buildbot.worker import AbstractLatentWorker


class DockerSwarmLatentWorker(AbstractLatentWorker):
    def __init__(self, name, image, *args, **kwargs):
        """
        Construct a ``DockerSwarmLatentWorker`` instance.

        :param name: Botname this machine will supply when it connects.
            This is passed to the worker image as WORKERNAME.

        :param image: Name of Docker image for buildbot worker.

        :param masterFQDN: Fully-qualified domain name of buildbot master.  This
            is passed as BUILDMASTER in the buildbot worker environment. By
            default, socket.getfqdn is used.  This can include a port
            specification, which is passed as BUILDMASTER_PORT.

        :param max_builds: Maximum number of simultaneous builds that will be
            run concurrently on this worker (the default is None for no limit)

        :param properties: properties that will be applied to builds run on this
            worker

        :param defaultProperties: properties that will be applied to builds run
            on this worker only if the property has not been set by another
            source

        :param locks: A list of locks that must be acquired before this worker
            can be used

        :param build_wait_timeout: Time in seconds to wait for build to start
        """
        password = kwargs.pop("password", None)
        super().__init__(name, password, *args, **kwargs)
        self.image = image
