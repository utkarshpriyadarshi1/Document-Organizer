package org.sanchaya.repository;

import org.sanchaya.model.BackupRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BackupRepository extends JpaRepository<BackupRecord, Long> {
}
