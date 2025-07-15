import lamindb as ln

ln.track()  # track the run of a script or notebook
open("sample.fasta", "w").write(">seq1\nACGT\n")
ln.Artifact("sample.fasta", key="sample.fasta").save()  # create a versioned artifact
ln.finish()  # finish the run, save source code & run report
