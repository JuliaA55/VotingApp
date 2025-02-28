// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public manager;
    
    struct Candidate {
        string name;
        uint voteCount;
    }
    
    mapping(string => Candidate) private candidates;
    mapping(address => bool) private hasVoted;
    string[] private candidateNames;

    event CandidateAdded(string name);
    event Voted(string candidate, address voter);
    event WinnerDeclared(string winner);

    constructor() {
        manager = msg.sender;
    }

    // Додавання кандидата (платна послуга)
    function addCandidate(string memory name) public payable {
        require(msg.sender == manager, "Only the manager can add candidates");
        require(bytes(candidates[name].name).length == 0, "Candidate already exists!");
        require(msg.value >= 0.01 ether, "Adding a candidate costs 0.01 ETH");

        candidates[name] = Candidate(name, 0);
        candidateNames.push(name);

        emit CandidateAdded(name);
    }

    // Голосування (тільки один раз)
    function vote(string memory candidate) public {
        require(!hasVoted[msg.sender], "You have already voted");
        require(bytes(candidates[candidate].name).length != 0, "Candidate does not exist!");

        candidates[candidate].voteCount++;
        hasVoted[msg.sender] = true;

        emit Voted(candidate, msg.sender);
    }

    // Переможець (лише власник)
    function getWinner() public view returns (string memory) {
        require(msg.sender == manager, "Only the manager can determine the winner");

        string memory winner;
        uint highestVotes = 0;

        for (uint i = 0; i < candidateNames.length; i++) {
            if (candidates[candidateNames[i]].voteCount > highestVotes) {
                highestVotes = candidates[candidateNames[i]].voteCount;
                winner = candidateNames[i];
            }
        }

        return winner;
    }

    // Перевірити баланс контракту
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Вивести гроші (лише власник)
    function withdraw() public {
        require(msg.sender == manager, "Only the manager can withdraw funds");
        payable(manager).transfer(address(this).balance);
    }
}
