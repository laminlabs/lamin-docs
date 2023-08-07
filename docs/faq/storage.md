# Storage FAQ

1. What is default storage? How do I find out about default storage?

2. Where is my SQLite file? What happens if I move the `.lndb` file around?

3. What is the `.lamindb/` folder? Will there be multiple `.lamindb/` folders if I have multiple storage locations?

4. What happens if I move files around? What should I do if I want to bulk migrate files to another storage (let’s say another s3 bucket)?

5. When should I pass `key=` and when should I rely on cryptic ids to register a file? What’s the recommended process to register a file?

6. Will I never be able to find my file if I don’t give it a description? (should this even be allowed?)

7. What should I do if I have a local file and want to upload it to S3? (Shall I register a File first and upload it with `.save`, or shall I upload outside of Lamin before registering it?)

8. How to update a file in storage? What’s the process to update file records after I moved files around or updated files?

9. How do I version a file? Do I always make a new file record and a new transform if I want to track the parent files?
