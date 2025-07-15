import lamindb as ln

ln.track()  # track the run of a script or notebook
open("sample.fastq", "w").write("@r1\nACGT\n+\nIIII\n")
ln.Artifact("sample.fastq", key="sample.fastq").save()  # create a versioned artifact
ln.finish()  # finish the run, save source code & run report
