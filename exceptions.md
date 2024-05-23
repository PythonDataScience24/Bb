## Where did we use exceptions?

We used exceptions in the code where we load and write files to disk. Since reading or writing can sometimes not work correctly if the file is damaged or the hardware resource to write the data to (HDD) is busy or has failed or been removed.

## How did we deal with exceptions?

When loading the database from disk if an exception occurs i.e. the database was lost since last run or is corrupted or similar we print a message to the console and then continue to launch the application by creating a new empty database in RAM. Next time this is changed we write it back down to disk.

When writing the database down to disk the error is harder to handle. Since if we can't write the database to disk the data will be gone after the application is closed. Thus we inform the user about the issue on the console output and the just continue running the application an keeping the new changes only in the database in RAM. Next time something is changed another write attempt is performed. If this succeeds then the previous changes will be written to disk too. Such a scenario might be likely if the HDD is temporarily so busy that it can't take our write request. 
